import "./App.css";
import { Form, Card, Container } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { useState } from "react";
import ModalError from "./components/ModalError";

function App() {
  const [activities, setActivities] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [error, setError] = useState("");
  const [notFound, setNotFound] = useState("");

  const getSuggestions = async (e) => {
    const values = e.target.value.split(/,/);
    let data = new FormData();
    data.append("city", values[0]);

    const res = await fetch("/city", {
      method: "POST",
      body: data,
    });

    if (res.status === 200) {
      const suggestionsJson = await res.json();
      setSuggestions(suggestionsJson);
      return true;
    }
    if (res.status === 404) {
      const resNotFound = await res.text();
      setSuggestions([]);
      setNotFound(resNotFound);
      return true;
    }
    const error = await res.text();
    console.log(error);
    setError(error);
    return true;
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    setNotFound("");
    const city = e.target.value;
    if (!city || city.length < 3) return true;
    const cityValues = city.split(/,/);
    if (cityValues.length < 3) {
      getSuggestions(e);
      return true;
    }
    setSuggestions([]);
    let data = new FormData();
    data.append("city", cityValues[0]);
    data.append("state", cityValues[1]);
    data.append("country", cityValues[2]);

    const resActivities = await fetch("/activities", {
      method: "POST",
      body: data,
    });

    if (resActivities.status === 200) {
      e.target.value = "";
      const jsonActivities = await resActivities.json();
      console.log(jsonActivities);
      setActivities(jsonActivities);
      return true;
    }
    const error = await resActivities.text();
    console.log(error);
    setError(error);
    return true;
  };

  return (
    <div classname="pb-5">
      <section className=" text-center m-2">
        <Container className="p-3 bg-light text-dark d-sm-flex justify-content-center align-items-center border rounded">
          <Form onSubmit={(e) => e.preventDefault()}>
            <Form.Label>Find and activity to do in your city!</Form.Label>
            <Form.Control
              type="text"
              placeholder="Ex: Rio de Janeiro"
              list="cityList"
              aria-describedby="notfound"
              onChange={(e) => {
                onSubmit(e);
              }}
            />
            <Form.Text id="notfound">{notFound ? notFound : " "}</Form.Text>
            <datalist id="cityList">
              {suggestions.map((response) => {
                return (
                  <option
                    key={`${Math.random()}`}
                    value={`${response[0]}, ${response[1]}, ${response[2]}`}
                  ></option>
                );
              })}
            </datalist>
          </Form>
        </Container>
      </section>
      <section className="text-center m-2">
        <Container className="p-3 bg-light text-dark d-sm-flex justify-content-center align-items-center border rounded">
          {activities.length !== 0 ? (
            <Container className="row">
              <Container fluid="sm">
                <h6>
                  At {activities["city"]} {activities["state"]}{" "}
                  {activities["country"]} the weather is:{" "}
                  {activities["weather"]}!
                </h6>
                <p>Founded {activities["activities"].length} activities:</p>
              </Container>
              <Container fluid="sm">
                {activities["activities"].map((activity) => {
                  return (
                    <Container>
                      <Card>
                        <h6>Activity: {activity.activity_title}</h6>
                        <h6>
                          Suggested Location: {activity.suggested_location}
                        </h6>
                        <h6>
                          Cost:{" "}
                          {activity.requisites.cost
                            ? activity.requisites.cost
                            : "Free"}
                        </h6>
                        <h6>
                          Number of participants:{" "}
                          {activity.requisites.participants_number}
                        </h6>
                      </Card>
                    </Container>
                  );
                })}
              </Container>
            </Container>
          ) : (
            " "
          )}
        </Container>
        <ModalError error={error} onHide={() => setError("")} />
      </section>
    </div>
  );
}

export default App;
