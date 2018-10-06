// Create the canvas size to our background image
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");
document.body.appendChild(canvas);

// Background image
var bgReady = false;
var bgImage = new Image();
bgImage.onload = function ()
{
  bgReady = true;
  // resize canvas to match bgImage size
  canvas.width = bgImage.width;
  canvas.height = bgImage.height;
};
bgImage.src = "background.png";

// Robot image
var robotReady = false;
var robotImage = new Image();
robotImage.onload = function ()
{
  robotReady = true;
};
robotImage.src = "robot.png";

// Game objects
var robot =
{
  x: 0,  // inches
  y: 0,  // inches
  angle: 0,  // degrees
};

var mousePos =
{
  x: 0,  // inches
  y: 0,  // inches
};

// Handle keyboard controls
var keysDown = {};
addEventListener('keydown', function (evt)
{
  keysDown[evt.keyCode] = true;
}, false);
addEventListener('keyup', function (evt)
{
  delete keysDown[evt.keyCode];
}, false);

// Handle mouse controls
canvas.addEventListener('mousemove', function (evt) {
  mousePos = getMousePos(evt);
}, false);

var controlSet = 0;
var curve_lines = [];
var current_curve_line = 0;

function getMousePos(evt) {
  var rect = canvas.getBoundingClientRect();
  return {
    x: evt.clientX - rect.left,
    y: evt.clientY - rect.top
  };
}

function interpolate(pt1, pt2, ratio)
{
  var xd = pt2.x - pt1.x;
  var yd = pt2.y - pt1.y;
  xd *= ratio;
  xd += pt1.x;
  yd *= ratio;
  yd += pt1.y;
  return { x: xd, y: yd };
}

function lineLength(pt1, pt2)
{
  var xd = pt2.x - pt1.x;
  var yd = pt2.y - pt1.y;
  var l = Math.sqrt( xd**2 + yd**2 );
  return l;
}

function generateCurve()
{
  var working_points = [];
  var curve_points = [];

  curve_lines = [];  // delete any old curve line data

  // copy control points from controlSet to working points
  for(var p = 0; p < control_points[controlSet].length; p++) 
  {
    working_points.push(control_points[controlSet][p]);
  }

  if (working_points.length < 3)
  {
    // control points become curve points
    for(var p = 0; p < working_points.length; p++) 
    {
      curve_points.push(working_points[p]);
    }
  }
  else
  {
    // add inflections points at center of every line that's not a "end" line
    for(var p = 1; p < (working_points.length - 2); p += 2) 
    {
        var point = interpolate(working_points[p], working_points[p+1], 0.5); // half way
        working_points.splice(p+1, 0, point);
    }

    // for each set of 3 working points, generate curve points
    for(var p = 0; p < (working_points.length - 2); p += 2)
    {
        // calc "3/4" average length of 2 segments to use as estimate of curve length
        var l1 = lineLength(working_points[p], working_points[p+1]);
        var l2 = lineLength(working_points[p+1], working_points[p+2]);
        var avg_l = (l1 + l2) * 3 / 4;

        var num_segments = Math.round(avg_l / 10);  // try to do 10 inch segments
        num_segments = Math.max(num_segments, 3);  // always at least 3 segments

        // we're going to add two extra straight segments, 1 at start and 1 at end
        num_segments += 2;

        // add straight segment to start
        curve_points.push(working_points[p]);
        var ratio = 1 / num_segments;
        var a = interpolate(working_points[p], working_points[p+1], ratio);
        curve_points.push(a);

        for(var t = 1; t < num_segments; t++)
        {
            // generate interpolated control points
            var ratio = t / num_segments;
            var a = interpolate(working_points[p], working_points[p+1], ratio);
            var b = interpolate(working_points[p+1], working_points[p+2], ratio);

            // generate interpolated curve point
            var point = interpolate(a, b, ratio);
            curve_points.push(point);
        }

        // add straight segment to end
        var ratio = (num_segments - 1) / num_segments;
        var b = interpolate(working_points[p+1], working_points[p+2], ratio);
        curve_points.push(b);
        curve_points.push(working_points[p+2]);
    }
  }

  // for each pair of curve points, add a curve line
  for(var p = 0; p < (curve_points.length - 1); p++) 
  {
      // generate curve lines
      var pt1 = curve_points[p];
      var pt2 = curve_points[p+1];
      var xd = pt2.x - pt1.x;
      var yd = pt2.y - pt1.y;
      var angle = Math.atan2(yd, xd) * 180.0 / Math.PI;  // degrees
      var length = Math.sqrt( xd**2 + yd**2 );  // inches
      // don't add any zero length curve lines
      if (length > 0)
      {
        var l = curve_lines.length;  // count of number of curve lines
        // if first curve line or at a different angle then last
        if ((l == 0) || (curve_lines[l-1].angle != angle))
        {
          // add it to our list of curve lines
          var curve_line = { pt1: pt1, pt2: pt2, angle: angle, length: length };
          curve_lines.push(curve_line);
        }
        else
        {
          // it's not the first and it is at the same angle as previoius,
          // so we combine them.
          curve_lines[l-1].pt2 = pt2;
          curve_lines[l-1].length += length;
        }
      }
  }
}

// Update robot position based on key presses
var then = Date.now();
function update()
{
  // Calculate the time diff in ms since we last updated robot
  // position. Use this as a proxy (scaled) for distance traveled.
  // Date.now() returns time in milliseconds since epoch
  var now = Date.now();
  var delta = now - then;
  then = now;
  // calculate the distance we would move based on time
  delta *= 0.1;

  var radians = robot.angle * Math.PI / 180.0;  // convert robot angle to radians

  // calculate x and y deltas (distance traveled) based on robot angle
  var deltaX = Math.sin(radians) * delta;
  var deltaY = Math.cos(radians) * delta;

  if (38 in keysDown)  // Player holding up
  {
    robot.y += deltaX;
    robot.x += deltaY;
  }
  if (40 in keysDown)  // Player holding down
  {
    robot.y -= deltaX;
    robot.x -= deltaY;
  }
  if (37 in keysDown)  // Player holding left
  {
    robot.angle += 5.0; // ccw 5 degrees
  }
  if (39 in keysDown)  // Player holding right
  {
    robot.angle -= 5.0;  // cw 5 degrees
  }

  if (32 in keysDown)  // Player hit spacebar
  {
    // move robot to end of current curve line
    var i = Math.min(current_curve_line, curve_lines.length - 1);
    robot.x = curve_lines[i].pt2.x;
    robot.y = curve_lines[i].pt2.y;
    robot.angle = curve_lines[i].angle;
    current_curve_line++;  // move to next curve line

    // +8 so it takes a few spacebar presses to jump to next controlSet
    if (current_curve_line >= (curve_lines.length + 8))
    {
      controlSet++;  // move to next control point set
      if (controlSet >= control_points.length)
      {
        controlSet = 0;
      }
      current_curve_line = 0;
      // move robot to start of first curve line
      robot.x = curve_lines[current_curve_line].pt1.x;
      robot.y = curve_lines[current_curve_line].pt1.y;
      robot.angle = curve_lines[current_curve_line].angle;
      generateCurve();
    }
  }
};

// ALL OF OUR OBJECTS ARE STORED IN INCHES AND CCW DEGREES
// WITH ORIGIN BEING LOWER LEFT CORNER OF FIELD.
// THESE FUNCTIONS ADJUST EVERYTHING FOR CW RADIANS
// AND AN ORIGIN AT THE TOP LEFT.
var X_OFFSET = 242;
var Y_OFFSET = 682;
var INCH_TO_PIXELS_SCALE = 2.0;

function pt_to_inches(pt)
{
  var x = pt.x;
  var y = pt.y;
  // move (0,0) to background image lower left
  x = x - X_OFFSET;
  y = y - Y_OFFSET;
  y = -y;
  // points are inches, convert to pixels (1 in = 2 pixels)
  x = x / INCH_TO_PIXELS_SCALE;
  y = y / INCH_TO_PIXELS_SCALE;
  // round to nearest half inch
  x = Math.round(x * 10) / 10;
  y = Math.round(y * 10) / 10;
  return { x: x, y: y };
}

// Draw image centered on pt at angle rotated around its center
function drawImageAtAngle(image, pt, angle)
{
  var width = image.width;
  var height = image.height;
  var radians = angle * Math.PI / 180.0;
  // points are inches, convert to pixels (1 in = 2 pixels) };
  var x = pt.x * INCH_TO_PIXELS_SCALE;
  var y = pt.y * INCH_TO_PIXELS_SCALE;
  // move (0,0) to background image lower left
  x = x + X_OFFSET;
  y = -y + Y_OFFSET;
  // our angles are CCW positive, canvas is clockwise
  radians = -radians;
  // now draw it on canvas
  ctx.translate(x, y);
  ctx.rotate(radians);
  ctx.drawImage(image, -width / 2, -height / 2, width, height);
  ctx.rotate(-radians);
  ctx.translate(-x, -y);
}

function drawLine(pt1, pt2)
{
  // points are inches, convert to pixels (1 in = 2 pixels)
  var x1 = pt1.x * INCH_TO_PIXELS_SCALE;
  var y1 = pt1.y * INCH_TO_PIXELS_SCALE;
  var x2 = pt2.x * INCH_TO_PIXELS_SCALE;
  var y2 = pt2.y * INCH_TO_PIXELS_SCALE;
  // move (0,0) to background image lower left
  x1 = x1 + X_OFFSET;
  y1 = -y1 + Y_OFFSET;
  x2 = x2 + X_OFFSET;
  y2 = -y2 + Y_OFFSET;
  // now draw it on canvas
  ctx.beginPath();
  ctx.moveTo(x1,y1);
  ctx.lineTo(x2,y2);
  ctx.strokeStyle = "rgb(0, 0, 0)";
  ctx.stroke();
}

function drawPoint(pt)
{
  // points are inches, convert to pixels (1 in = 2 pixels)
  var x = pt.x * INCH_TO_PIXELS_SCALE;
  var y = pt.y * INCH_TO_PIXELS_SCALE;
  // move (0,0) to background image lower left
  x = x + X_OFFSET;
  y = -y + Y_OFFSET;
  // now draw it on canvas
  ctx.fillStyle = "rgb(250, 250, 250)";
  ctx.fillRect(x-2,y-2,5,5);
}

function writeMessage(message, x, y) {
  ctx.fillStyle = "rgb(250, 250, 250)";
  ctx.font = "24px Helvetica";
  ctx.textAlign = "left";
  ctx.textBaseline = "top";
  ctx.fillText(message, x, y);
}

// Draw everything
function render()
{
  if (bgReady)
  {
    ctx.drawImage(bgImage, 0, 0);
  }

  if (robotReady)
  {
    drawImageAtAngle(robotImage, robot, robot.angle);
  }

  // draw curve lines
  for (var i = 0; i < curve_lines.length; i++)
  {
    line = curve_lines[i];
    drawLine(line.pt1, line.pt2);
  }

  // draw control points
  for (var i = 0; i < control_points[controlSet].length; i++)
  {
    drawPoint(control_points[controlSet][i]);
  }

  // Some text output
  writeMessage('controlSet: ' + controlSet, 32, 32);
  var pt_inches = pt_to_inches(mousePos);
  writeMessage('mousePos: ' + pt_inches.x + ',' + pt_inches.y, 32, 54);
};

// Reset the game
function reset()
{
  // switch to first control set
  controlSet = 0;
  // generate curve lines for it
  generateCurve();
  current_curve_line = 0;
  // move robot to start of first curve line
  robot.x = curve_lines[0].pt1.x;
  robot.y = curve_lines[0].pt1.y;
  robot.angle = curve_lines[0].angle;
};

// The main game loop
function main()
{
  update();  // update robot position based on key presses
  render();  // draw graphics
  requestAnimationFrame(main);  // Request to do this again ASAP
};

// Cross-browser support for requestAnimationFrame
var w = window;
requestAnimationFrame = w.requestAnimationFrame || w.webkitRequestAnimationFrame || w.msRequestAnimationFrame || w.mozRequestAnimationFrame;

// Let's play this game!
reset();
main();
