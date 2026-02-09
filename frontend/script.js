async function getRecommendation() {
  const city = document.getElementById("city").value.trim();
  const output = document.getElementById("output");
  const loader = document.getElementById("loader");

  if (!city) {
    output.innerHTML = "❗ Please enter a city name.";
    return;
  }

  output.innerHTML = "";
  loader.classList.remove("hidden");

  try {
    const response = await fetch("http://localhost:3000/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ city })
    });

    const data = await response.json();

    loader.classList.add("hidden");

    output.innerHTML = `
      <h3>🌦️ Weather in ${data.weather.city}</h3>
      <p>🌡️ ${data.weather.temperature}°C | ${data.weather.condition}</p>

      <div class="outfit-box">
        <p><strong>👕 Top:</strong> ${data.recommendations.top}</p>
        <p><strong>👖 Bottom:</strong> ${data.recommendations.bottom}</p>
        <p><strong>👟 Footwear:</strong> ${data.recommendations.footwear}</p>
      </div>
    `;
  } catch (error) {
    loader.classList.add("hidden");
    output.innerHTML = "❌ Something went wrong. Try again.";
  }
}

async function fetchCities() {
  const input = document.getElementById("city").value.trim();
  const suggestionsDiv = document.getElementById("suggestions");

  if (input.length < 2) {
    suggestionsDiv.innerHTML = "";
    return;
  }

  const response = await fetch(
    `http://localhost:3000/cities?q=${encodeURIComponent(input)}`
  );
  const cities = await response.json();

  suggestionsDiv.innerHTML = cities
    .map(
      c => `<div onclick="selectCity('${c.name}')">${c.name}</div>`
    )
    .join("");
}

function selectCity(city) {
  document.getElementById("city").value = city;
  document.getElementById("suggestions").innerHTML = "";
}
