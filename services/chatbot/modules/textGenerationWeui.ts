export async function generateText(prompt: string): Promise<any> {
  const response = await fetch('http://localhost:50596/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  });

  return response.json();
}
