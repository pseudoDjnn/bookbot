window.addEventListener("DOMContentLoaded", () => {
  const dataElement = document.getElementById("results-data");
  const rawData = dataElement.textContent.trim();

  try {
    // Let's see what we're getting
    console.log("Raw data:", rawData);

    const data = JSON.parse(rawData);
    console.log("Parsed data:", data);

    const charCount = data.Results["Character Count"];
    console.log("Character count data:", charCount);

    const totalChars = Object.values(charCount).reduce((a, b) => a + b, 0);

    // Create results display
    const resultsDiv = document.createElement("div");
    resultsDiv.id = "text-results";
    resultsDiv.innerHTML = `<p>Total Characters: ${totalChars}</p>`;

    // Insert before the chart container
    const chartContainer = document.getElementById("chart-container");
    document.body.insertBefore(resultsDiv, chartContainer);

  } catch (error) {
    console.error("Raw data causing error:", rawData);
    console.error("Error parsing or displaying results:", error);
    const errorDiv = document.createElement("div");
    errorDiv.className = "error";
    errorDiv.textContent = "Error displaying results";
    document.body.appendChild(errorDiv);
  }
});