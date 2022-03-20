import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { useState, useEffect } from "react";
import { Form, Container } from "react-bootstrap";
import ModalError from "./components/ModalError";
import PopulatedList from "./components/PopulatedList";
import CityLabel from "./components/CityLable";
import CityResult from "./components/CityResult";
import Activities from "./components/Activities";

function App() {
  const [activities, setActivities] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [error, setError] = useState("");
  const [notFound, setNotFound] = useState("");
  const [loading, setLoading] = useState(false);
  const [weatherList, setWeatherList] = useState([]);
  const [particpantsNumberList, setParticipantsNumberList] = useState([]);
  const [costsList, setCostsList] = useState([]);

  useEffect(() => {
    //Fetch Tasks
    const fetchActivitiesUniqueValues = async () => {
      const res = await fetch("/getactivitiesuiniquevalues", {
        method: "POST",
      });
      const data = await res.json();
      setWeatherList(data.activities_weather);
      setParticipantsNumberList(data.activities_participants_number);
      setCostsList(data.activities_costs);
    };
    fetchActivitiesUniqueValues();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const getSuggestions = async (str) => {
    if (!str || str.length < 3) return true;
    const values = str.split(/,/);
    let data = new FormData();
    data.append("city", values[0]);
    const res = await fetch("/citieslist", {
      method: "POST",
      body: data,
    });
    if (res.status === 200) {
      const suggestionsJson = await res.json();
      setSuggestions(suggestionsJson);
      suggestionsJson.length === 0
        ? setNotFound("City not found")
        : setNotFound("");
      return true;
    }
    const error = await res.text();
    console.log(error);
    setError(error);
    return true;
  };

  const onSelectCity = (str) => {
    const city = str;
    const cityValues = city.split(/,/);
    setSuggestions([]);
    setLoading(true);
    let data = new FormData();
    data.append("city", cityValues[0]);
    data.append("state", cityValues[1]);
    data.append("country", cityValues[2]);

    fetchActivities("/getactivitiesbycity", data);
  };

  const onSelectWeather = (str) => {
    let data = new FormData();
    data.append("weather", str);
    fetchActivities("/getactivitiesbyweather", data);
  };

  const onSelectParticipantsNumber = (str) => {
    let data = new FormData();
    data.append("participants_number", parseInt(str));
    fetchActivities("/getactivitiesbyparticipantsnumber", data);
  };

  const onSelectCost = (str) => {
    let data = new FormData();
    data.append("cost", str);
    fetchActivities("/getactivitiesbycost", data);
  };

  const fetchActivities = async (resource, data) => {
    setLoading(true);
    const resActivities = await fetch(resource, {
      method: "POST",
      body: data,
    });
    setLoading(false);
    if (resActivities.status === 200) {
      const jsonActivities = await resActivities.json();
      setActivities(jsonActivities);
      return true;
    }
    const error = await resActivities.text();
    console.log(error);
    setError(error);
    return true;
  };

  return (
    <div className="pb-5">
      <section className=" text-center m-2">
        <Container className="p-3 bg-light text-dark d-sm-flex justify-content-center align-items-center border rounded">
          <Form>
            <PopulatedList
              caption="Weather"
              optionList={weatherList}
              onChange={onSelectWeather}
            />
            <PopulatedList
              caption="Number of participants"
              optionList={particpantsNumberList}
              onChange={onSelectParticipantsNumber}
            />
            <PopulatedList
              caption="Cost"
              optionList={costsList}
              onChange={onSelectCost}
            />
            <CityLabel
              caption="City name"
              onChange={getSuggestions}
              notFound={notFound}
              loading={loading}
            />
            <CityResult suggestions={suggestions} onSelectCity={onSelectCity} />
          </Form>
        </Container>
      </section>
      {activities.length !== 0 || loading ? (
        <Activities loading={loading} activities={activities} />
      ) : (
        " "
      )}
      <ModalError error={error} onHide={() => setError("")} />
    </div>
  );
}

export default App;
