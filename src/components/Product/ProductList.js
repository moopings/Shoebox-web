import React, { PropTypes } from 'react'
import { Grid } from 'react-bootstrap'

const ProductList = ({title, children}) => (
  <Grid>
    <h1>{title}</h1>
    <div>{children}</div>
  </Grid>
)

ProductList.propTypes = {
  children: PropTypes.node,
  title: PropTypes.string.isRequired
}

export default ProductList
