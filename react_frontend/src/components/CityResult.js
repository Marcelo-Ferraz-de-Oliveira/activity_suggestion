import React from "react";
import {Container } from "react-bootstrap";


const CityResult = ({ suggestions, onSelectCity }) => {
  return (
    <Container id="cityList">
      {suggestions.map((response) => {
        return (
          <p
            key={`${Math.random()}`}
            onClick={() => {
              onSelectCity(`${response[0]}, ${response[1]}, ${response[2]}`);
            }}
          >
            {`${response[0]}, ${response[1]}, ${response[2]}`}
          </p>
        );
      })}
    </Container>
  );
};

export default CityResult;
