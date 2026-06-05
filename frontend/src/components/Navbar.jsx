import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 text-white p-4 flex gap-6">

      <Link to="/dashboard">
        Dashboard
      </Link>

      <Link to="/products">
        Products
      </Link>

      <Link to="/customers">
        Customers
      </Link>

      <Link to="/orders">
        Orders
      </Link>

    </nav>
  );
}

export default Navbar;