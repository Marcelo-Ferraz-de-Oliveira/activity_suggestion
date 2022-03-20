import React from "react";
import { Form } from "react-bootstrap";

const PopulatedList = ({ caption, optionList, onChange }) => {
  return (
    <Form.Group>
      <Form.Label>{caption}</Form.Label>
      <Form.Select aria-label="" onChange={(e) => onChange(e.target.value)}>
        <option>Select option</option>
        {optionList.map((option) => {
          return <option key={`${Math.random()}`} value={option}>{option}</option>;
        })}
      </Form.Select>
    </Form.Group>
  );
};

export default PopulatedList;
