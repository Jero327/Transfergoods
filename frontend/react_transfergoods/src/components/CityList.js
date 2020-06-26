import React, { Component } from "react";
import { Table } from "reactstrap";
import NewCityModal from "./NewCityModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class CityList extends Component {
  render() {
    const citys = this.props.citys;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!citys || citys.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Let's add some citys</b>
              </td>
            </tr>
          ) : (
            citys.map(city => (
              <tr key={city.pk}>
                <td>{city.name}</td>
                <td align="center">
                  <NewCityModal
                    create={false}
                    city={city}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={city.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default CityList;