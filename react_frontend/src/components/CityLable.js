import React from "react";
import { Form } from "react-bootstrap";

const CityLabel = ({ caption, onChange, notFound, loading }) => {
  return (
<Form.Group >

<Form.Label>{caption}</Form.Label>
<Form.Control
  type="text"
  placeholder="Ex: Manaus"
  list="cityList"
  aria-describedby="notfound"
  onChange={(e) => {
    onChange(e.target.value);
  }}
  />
<Form.Text id="notfound">{notFound ? notFound : " "}</Form.Text>
{loading}
</Form.Group>
  );
};

export default CityLabel;
