import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewCityForm extends React.Component {
  state = {
    pk: 0,
    name: ""
  };

  componentDidMount() {
    if (this.props.city) {
      const { pk, name } = this.props.city;
      this.setState({ pk, name });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createCity = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editCity = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.city ? this.editCity : this.createCity}>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>
        <Button>Save</Button>
      </Form>
    );
  }
}

export default NewCityForm;