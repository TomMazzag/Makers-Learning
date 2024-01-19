const Weather = require("./weather");
const WeatherClient = require("./weatherClient");

describe("Test weather class", () => {
  test("Test get data", async () => {
    const client = new WeatherClient();
    const weather = new Weather(client);

    await weather.load("Bristol");
    expect(weather.getWeatherData()).toEqual({
      City: "Bristol",
      Weather: "Clear",
      Temperature: -9,
      Feels_like: -9,
      Humidity: "67%",
    });
  });
});
