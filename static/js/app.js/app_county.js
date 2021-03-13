// Get a reference to the table body
var tbody = d3.select("tbody");

// Use d3 to update each cell's text with report values
data.forEach(function(property) {
  var row = tbody.append("tr");
  Object.entries(property).forEach(function([key, value]) {

    // Append a cell to the row for each value
    // in the report object

    var cell = row.append("td");
    cell.text(value);
  });
});

// Use a county form in your HTML document and write JavaScript code that will search through the county column to find rows that match

// Assign the data from data.js to a descriptive variable
var tableData = data;

// Select the button
var button = d3.select("#filter-btn");

// Select the form
var form = d3.select('form');

// Create event handlers
button.on("click", submitForm);
form.on("submit", submitForm);

// Complete the event handler function for the form
function submitForm() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select('#countyInput');

  // Get the value property of the input element
  var inputValue = inputElement.property('value');

  console.log(inputValue);
  // console.log(tableData);

  var filteredData = tableData.filter(property => property.County_Name === inputValue);

  // console.log(filteredData);

  // Clear current table body
  d3.select('tbody').text('');

  // Get a reference to the table body and save to new variable
  var filterTbody = d3.select("tbody");

  // Create table pulling information matching the filter
  filteredData.forEach(function(property) {
  // console.log(property);
  var row = filterTbody.append("tr");
  Object.entries(property).forEach(function([key, value]) {
    // console.log(key, value);

    var cell = row.append("td");
    cell.text(value);
  });
});
};
