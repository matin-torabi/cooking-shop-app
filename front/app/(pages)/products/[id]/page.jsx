import ProductDetail from "@/modules/products/components/ProductDetail";

const page = async ({ params }) => {
  const data = await params;
  const { id } = data;
  return (
    <>
      <ProductDetail id={id}/>
    </>
  );
};

export default page;
