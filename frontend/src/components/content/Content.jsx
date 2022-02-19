import React from "react";
import {
  Box,
  Toolbar,
  Grid,
  Container,
  Typography,
  CardContent,
  Card,
} from "@mui/material";

function Content(props) {
  return (
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        p: 4,
        width: { sm: `calc(100% - ${props.drawerWidth}px)` },
      }}
    >
      <Toolbar />
      {props.children}
    </Box>
  );
}

export default Content;
