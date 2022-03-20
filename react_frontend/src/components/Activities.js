import React from 'react'
import { Card, Container, Spinner } from "react-bootstrap";

const Activities = ({loading, activities}) => {
  return (
    <section className="text-center m-2">
        <Container className="p-3 bg-light text-dark d-sm-flex justify-content-center align-items-center border rounded">
          {loading === true ? (
            <Spinner animation="border" role="status">
              <span className="visually-hidden">Loading...</span>
            </Spinner>
          ) : (
            
          
            <Container className="row">
              <Container fluid="sm">
                {activities["city"] ? (<h6>
                  At {activities["city"]} {activities["state"]}{" "}
                  {activities["country"]} the weather is:{" "}
                  {activities["weather"]}!
                </h6>): (" ")}
                <p>Found {activities["activities"].length} activities:</p>
              </Container>
              <Container fluid="sm">
                {activities["activities"].map((activity) => {
                  return (
                    <Container key={activity.id}>
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
          
          )}
        </Container>
      </section>
  )
}

export default Activities