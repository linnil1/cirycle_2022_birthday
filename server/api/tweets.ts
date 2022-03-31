export default async (req, res) => {
  // cloudflare: read from KV
  if (typeof cirycle_2022_birthday !== 'undefined') {
    const value = await cirycle_2022_birthday.get("tweets_cirycle.json", {type: "json"});
    return value;
  }
  // local: read from data.py
  const url = "http://192.168.208.206:8081/api/tweets"
  const response = await fetch(url, {method: "POST"});
  return response.json();
}
