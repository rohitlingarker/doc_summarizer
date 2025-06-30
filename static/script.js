document.getElementById('uploadForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const file = document.getElementById('document').files[0];
  const rawText = document.getElementById('raw_text').value.trim();
  const formData = new FormData();

  if (file) {
    formData.append('document', file);
  }
  if (rawText) {
    formData.append('raw_text', rawText);
  }

  const res = await fetch('/summarize', {
    method: 'POST',
    body: formData
  });

  const data = await res.json();
  document.getElementById('summary').innerText = marked(data.summary) || data.error || "No response.";
});
