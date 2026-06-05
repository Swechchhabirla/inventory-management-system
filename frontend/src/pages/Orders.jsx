import { useEffect, useState } from "react";
import API from "../services/api";

function Orders() {

  const [orders, setOrders] = useState([]);

  const [customerId, setCustomerId] = useState("");
  const [productId, setProductId] = useState("");
  const [quantity, setQuantity] = useState("");

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {

      const response = await API.get("/orders");

      setOrders(response.data);

    } catch (error) {

      console.log(error);

    }
  };

  const createOrder = async (e) => {

    e.preventDefault();

    try {

      await API.post("/orders", {
        customer_id: Number(customerId),
        items: [
          {
            product_id: Number(productId),
            quantity: Number(quantity)
          }
        ]
      });

      fetchOrders();

      setCustomerId("");
      setProductId("");
      setQuantity("");

    } catch (error) {

      console.log(error);

      alert("Unable to create order");

    }
  };

  return (
    <div>

      <h1>Orders</h1>

      <form onSubmit={createOrder}>

        <input
          type="number"
          placeholder="Customer ID"
          value={customerId}
          onChange={(e) =>
            setCustomerId(e.target.value)
          }
        />

        <input
          type="number"
          placeholder="Product ID"
          value={productId}
          onChange={(e) =>
            setProductId(e.target.value)
          }
        />

        <input
          type="number"
          placeholder="Quantity"
          value={quantity}
          onChange={(e) =>
            setQuantity(e.target.value)
          }
        />

        <button type="submit">
          Create Order
        </button>

      </form>

      <br />

      <table border="1">

        <thead>

          <tr>
            <th>ID</th>
            <th>Customer ID</th>
            <th>Total Amount</th>
          </tr>

        </thead>

        <tbody>

          {orders.map((order) => (

            <tr key={order.id}>

              <td>{order.id}</td>

              <td>{order.customer_id}</td>

              <td>{order.total_amount}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Orders;