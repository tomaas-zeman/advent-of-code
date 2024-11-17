import fs from 'fs';

const SESSION = fs.readFileSync('.session', 'utf-8').trim();

export async function postAnswer(year: string, day: string, part: string, answer: string) {
  const response = await fetch(`https://adventofcode.com/${year}/day/${parseInt(day, 10)}/answer`, {
    headers: { Cookie: `session=${SESSION}`, 'Content-Type': 'application/x-www-form-urlencoded' },
    method: 'POST',
    body: new URLSearchParams({ level: part, answer }).toString(),
  });

  if (!response.ok) {
    throw new Error(`Failed to submit the answer: ${response.status} ${response.statusText}`);
  }

  return response;
}

export async function fetchInputData(year: string, day: string) {
  const response = await fetch(`https://adventofcode.com/${year}/day/${parseInt(day, 10)}/input`, {
    headers: {
      Cookie: `session=${SESSION}`,
    },
  });

  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }

  return response;
}
