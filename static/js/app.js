window.addEventListener("DOMContentLoaded", () => {
  // Fetch raw JSON data from the DOM
  const dataElement = document.getElementById("results-data");
  const rawData = dataElement.textContent.trim();
  // console.log("Loaded Raw JSON from DOM:", rawData);

  // Attempt to parse the JSON
  try {
    const parsedData = JSON.parse(JSON.parse(rawData)); // Parse twice for nested structure
    // console.log("Parsed Data Object:", parsedData);

    // Access the "Results" key specifically
    const results = parsedData.Results; // Extract the nested "Results" key
    console.log("Processing Results:", results);

    // Render the word count
    if ("Total Word Count" in results) {
      renderWordCount(results["Total Word Count"]);
    } else {
      console.warn("No 'Total Word Count' key found in Results.");
    }
  } catch (error) {
    console.error("Failed to parse JSON data:", error);
  }
});

// Render the word count using fetched data
function renderWordCount(wordCount) {
  // Find or create an element where you want to display the word count
  let wordCountElement = document.getElementById("word-count");

  if (!wordCountElement) {
    // If the element doesn't exist, create it dynamically
    wordCountElement = document.createElement("div");
    wordCountElement.id = "word-count";
    document.body.appendChild(wordCountElement);
  }

  // Update the content of the element
  wordCountElement.textContent = `Total Word Count: ${wordCount}`;
}