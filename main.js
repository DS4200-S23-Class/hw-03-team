// Initialize array with different font families
const fontsList = ["Times New Roman", "Comic Sans MS", "Chalkduster",
    "Brush Script MT", "Bradley Hand", "Apple Chancery",
    "Copperplate", "Courier New", "Didot", "Geneva", "Gill Sans",
    "Luminari", "Marker Felt", "Arial"];

// Initialize counter to iterate through array
let counter = 0;

// Create text that will remain the same throughout function
const fontText = " is a nice font, but...";


// Function used to change the font on click
function changeFont() {

    // Checks if counter is past the length of array
    // If so, reset to 0 --> loop over the list again
    if (counter > fontsList.length - 1) {
        counter = 0;
    }

    // Change the font of the website in order of the list
    document.body.style.fontFamily = fontsList[counter];

    // Create new statement for above button
    let finalStatement = fontsList[counter].concat(fontText);

    // Return the final statement and updates html
    document.getElementById("button-text").innerHTML = finalStatement;

    // Add to counter
    counter++;

}