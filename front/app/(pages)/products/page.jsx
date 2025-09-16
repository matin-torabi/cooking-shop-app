import Navbar from "@/app/components/Navbar/Navbar";
import ProductView from "@/modules/products/view/ProductView";

const products = () => {
  return(
    <>
      <Navbar />
      <ProductView />;
    </>
  ) 
};

export default products;
