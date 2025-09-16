import Paginatio from "../components/Pagination";
import ProductItem from "../components/ProductItem";

const ProductView = () => {
  return (
    <>
      <div className="w-full flex flex-col gap-10 items-center mt-[100px]">
        <div className="w-full flex flex-wrap gap-5 justify-center">
          <ProductItem />
        </div>
      </div>

    </>
  );
};

export default ProductView;
