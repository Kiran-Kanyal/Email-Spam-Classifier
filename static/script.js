async function analyzeEmail() {
  const emailText = document.getElementById("inputText").value; // Get email text from input field
  const response = await fetch("/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: emailText }), // Send the email text in the request body
  });
  const result = await response.json();
  document.getElementById("result").innerText = `Result: ${result.result}`; // Display the classification result
}
