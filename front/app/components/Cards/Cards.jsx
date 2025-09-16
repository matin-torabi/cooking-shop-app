import Card from "./Card";

const Cards = () => {
    return ( 
        <section className="mobile:w-full laptop:w-[90%] desktop:w-[70%] h-auto my-10 flex flex-wrap items-center justify-center mx-auto gap-5">
            <Card/>
        </section>

    );
}
 
export default Cards;