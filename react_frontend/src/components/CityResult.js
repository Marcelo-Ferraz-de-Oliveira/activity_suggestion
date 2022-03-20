import React from "react";
import { ListGroup } from "react-bootstrap";

const CityResult = ({ suggestions, onSelectCity }) => {
  return (
    <ListGroup id="cityList">
      {suggestions.map((response) => {
        return (
          <ListGroup.Item
            action
            key={`${Math.random()}`}
            onClick={() => {
              onSelectCity(`${response[0]}, ${response[1]}, ${response[2]}`);
            }}
          >
            {`${response[0]}, ${response[1]}, ${response[2]}`}
          </ListGroup.Item>
        );
      })}
    </ListGroup>
  );
};

export default CityResult;
