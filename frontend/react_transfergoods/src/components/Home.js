import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import CityList from "./CityList";
import NewCityModal from "./NewCityModal";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    citys: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCitys = () => {
    const options = {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8'
      }
    };
    fetch(API_URL, options).then(res => res.json()).then(res => this.setState({ citys: res }));
  };

  resetState = () => {
    this.getCitys();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <CityList
              citys={this.state.citys}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewCityModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;