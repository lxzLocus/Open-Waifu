export async function generateImage(prompt: string): Promise<any> {
  const response = await fetch('http://localhost:57549/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt })
  });

  return response.json();
}
