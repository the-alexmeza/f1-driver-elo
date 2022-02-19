import React from "react";
import { Grid, Card, CardContent, Typography, Container } from "@mui/material";
import {
  TableRow,
  Paper,
  TableContainer,
  Table,
  TableHead,
  TableCell,
  TableBody,
} from "@mui/material";

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const rows = [
  createData("Frozen yoghurt", 159, 6.0, 24, 4.0),
  createData("Ice cream sandwich", 237, 9.0, 37, 4.3),
  createData("Eclair", 262, 16.0, 24, 6.0),
  createData("Cupcake", 305, 3.7, 67, 4.3),
  createData("Gingerbread", 356, 16.0, 49, 3.9),
];

const tempTable = (
  <TableContainer component={Paper} sx={{ p: 4 }}>
    <Table sx={{ minWidth: 650, overflowX: "auto" }} aria-label="simple table">
      <TableHead>
        <TableRow>
          <TableCell>Dessert</TableCell>
          <TableCell align="right">Calories</TableCell>
          <TableCell align="right">Fat (g)</TableCell>
          <TableCell align="right">Carbs (g)</TableCell>
          <TableCell align="right">Protein (g)</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {rows.map((row) => (
          <TableRow
            key={row.name}
            sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
          >
            <TableCell component="th" scope="row">
              {row.name}
            </TableCell>
            <TableCell align="right">{row.calories}</TableCell>
            <TableCell align="right">{row.fat}</TableCell>
            <TableCell align="right">{row.carbs}</TableCell>
            <TableCell align="right">{row.protein}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  </TableContainer>
);

function Drivers() {
  return (
    <Grid container spacing={4}>
      <Grid item sm={8} xs={12}>
        {tempTable}
      </Grid>
      <Grid item sm={4} xs={12}>
        <Card component={Container}>
          <CardContent>
            <Typography paragraph>Test text!</Typography>
          </CardContent>
        </Card>
        <br></br>
        {tempTable}
      </Grid>
    </Grid>
  );
}

export default Drivers;
