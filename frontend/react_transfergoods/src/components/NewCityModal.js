import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewCityForm from "./NewCityForm";

class NewCityModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Edit City";
    var button = <Button onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Create New City";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Create New
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewCityForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              city={this.props.city}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewCityModal;