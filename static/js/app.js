window.addEventListener("DOMContentLoaded", () => {
  // Get the analysis results element
  const analysisResults = document.getElementById("analysis-results");
  if (!analysisResults) return;

  // Get the analysis type
  const analysisType = analysisResults.dataset.analysisType;
  console.log("Analysis type:", analysisType);

  // If we have word count data (either directly or as part of 'all')
  if (analysisType === "word_count" || analysisType === "all") {
    // Find the paragraph with the word count
    const wordCountPara = analysisResults.querySelector("p:contains('Total Words:')");
    if (wordCountPara) {
      // Extract and log the count
      const count = wordCountPara.textContent.replace("Total Words:", "").trim();
      console.log("Word count from page:", count);

      // You could add styling or additional content here if needed
      wordCountPara.style.fontWeight = "bold";
    }
  }
});