import "./App.css";
import Dashboard from "./components/Dashboard";
import { CssBaseline } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";

function App() {
  let theme = createTheme({
    palette: {
      type: "light",
      primary: {
        main: "#1b2441",
      },
      secondary: {
        main: "#c22636",
      },
      success: {
        main: "#01804f",
      },
      background: {
        default: "#F7F9FF",
      },
      info: {
        main: "#1c3d72",
      },
    },
  });
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <CssBaseline enableColorScheme />
        <Dashboard />
      </ThemeProvider>
    </div>
  );
}

export default App;
