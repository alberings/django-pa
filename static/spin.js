// Assuming theWinwheel.js library is already included in your HTML.

// Define the spinning wheel with no segments first.
var theWheel = new Winwheel({
    'outerRadius' : 212,   // Set the outer radius so the wheel fits inside the background.
    'textFontSize' : 28,   // Set font size as desired.
    'animation' : {        // Specify the animation to use.
        'type'     : 'spinToStop',
        'duration' : 5,     // Duration in seconds.
        'spins'    : 8,     // Number of complete spins.
        'callbackFinished' : alertPrize
    }
});

// Function to handle the result of the spin.
function alertPrize(indicatedSegment) {
    // This is called when the animation has finished.
    alert("The wheel stopped on " + indicatedSegment.text);
}

// Function to add segments to the wheel.
function addSegment(segmentText) {
    var segment = {'fillStyle' : randomColor(), 'text' : segmentText};
    theWheel.addSegment(segment);
    theWheel.draw();
}

// Function to generate a random color - just for fun.
function randomColor() {
    return '#' + Math.floor(Math.random()*16777215).toString(16);
}

// Click handler for spin button.
document.getElementById('spinButton').addEventListener('click', function() {
    theWheel.startAnimation();
});

// Function to remove a segment from the wheel.
function removeSegment(segmentIndex) {
    theWheel.deleteSegment(segmentIndex);
    theWheel.draw();
}

// Function to dynamically update the wheel with new items.
function updateWheel(itemsArray) {
    // Clear the wheel
    theWheel.clearSegments();
    
    // Add each item to the wheel
    itemsArray.forEach(function(item) {
        addSegment(item);
    });
    
    // Redraw the wheel
    theWheel.draw();
}

document.addEventListener('DOMContentLoaded', function() {
    var itemsJson = document.getElementById('items-json').textContent;
    var items = JSON.parse(itemsJson);
    // Now you can use 'items' to populate the wheel
});



// This could be triggered on a form submit event or a button click
// assuming itemsArray comes from your server or form input.
// updateWheel(['Item 1', 'Item 2', 'Item 3', ...]);
