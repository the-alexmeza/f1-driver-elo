import {
  TableRow,
  Card,
  Paper,
  TableContainer,
  Table,
  TableHead,
  TableCell,
  Typography,
  TableBody,
} from "@mui/material";
import React, { Component } from "react";
import Navigation from "./navigation/Navigation";
import Drivers from "./drivers/Drivers";

class Dashboard extends Component {
  state = {};

  render() {
    return (
      <>
        <Navigation>
          <Drivers></Drivers>
        </Navigation>
      </>
    );
  }
}

export default Dashboard;
