import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import CityList from "./CityList";
import NewCityModal from "./NewCityModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    citys: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCitys = () => {
    axios.get(API_URL).then(res => this.setState({ citys: res.data }));
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