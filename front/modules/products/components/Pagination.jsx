'use client'
// import React from 'react';
// import { Pagination } from 'antd';
// const onChange = pageNumber => {
//   console.log('Page: ', pageNumber);
// };
// const Paginatio = () => (
//   <>
//     <Pagination showQuickJumper defaultCurrent={2} total={500} onChange={onChange} />
//     <br />
//     <Pagination showQuickJumper defaultCurrent={2} total={500} onChange={onChange} disabled />
//   </>
// );
// export default Paginatio;

import React from 'react';
import { Pagination } from 'antd';
const Paginatio = () => <Pagination defaultCurrent={1} total={100} />;
export default Paginatio;