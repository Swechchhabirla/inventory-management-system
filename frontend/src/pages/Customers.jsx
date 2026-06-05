import { useEffect, useState } from "react";
import API from "../services/api";

function Customers() {

  const [customers, setCustomers] = useState([]);

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone: ""
  });

  useEffect(() => {
    fetchCustomers();
  }, []);

  const fetchCustomers = async () => {
    try {

      const response = await API.get("/customers");

      setCustomers(response.data);

    } catch (error) {

      console.log(error);

    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      await API.post("/customers", formData);

      fetchCustomers();

      setFormData({
        full_name: "",
        email: "",
        phone: ""
      });

    } catch (error) {

      console.log(error);

    }
  };

  return (
    <div>

      <h1>Customers</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          value={formData.full_name}
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />

        <input
          type="text"
          name="phone"
          placeholder="Phone"
          value={formData.phone}
          onChange={handleChange}
        />

        <button type="submit">
          Add Customer
        </button>

      </form>

      <br />

      <table border="1">

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
          </tr>
        </thead>

        <tbody>

          {customers.map((customer) => (

            <tr key={customer.id}>

              <td>{customer.id}</td>
              <td>{customer.full_name}</td>
              <td>{customer.email}</td>
              <td>{customer.phone}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Customers;