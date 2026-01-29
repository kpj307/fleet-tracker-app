import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import useDocumentTitle from "./hooks/useDocumentTitle";
import Layout from "./components/Layout";
import Login from "./pages/Login"
import Register from "./pages/Register"
import VehicleList from "./pages/VehicleList"
import VehicleDetails from "./pages/VehicleDetails"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  useDocumentTitle();

  return (
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
               <Layout>
                  <VehicleList />
               </Layout>
            </ProtectedRoute>
          }
        />
        <Route 
          path="/api/vehicles/:id" 
          element={
            <Layout>
              <VehicleDetails />
            </Layout>
          } 
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
  )
}

export default App
