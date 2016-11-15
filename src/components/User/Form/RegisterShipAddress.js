import React from 'react'
import { reduxForm, Field } from 'redux-form'
import RegisterRenderField from './RegisterRenderField'
import RegisterValidate from './RegisterValidate'

const RegisterShipAddress = (props) => {
  const {
    handleSubmit,
    previousPage,
    invalid,
    submitting
  } = props

  return (
    <form onSubmit={handleSubmit}>

      <Field
        name="ship.city"
        component={RegisterRenderField}
        type="text"
        label="City"/>

      <Field
        name="ship.district"
        component={RegisterRenderField}
        type="text"
        label="District"/>

      <Field
        name="ship.street"
        component={RegisterRenderField}
        type="text"
        label="Street"/>

      <Field
        name="ship.zipcode"
        component={RegisterRenderField}
        type="text"
        label="Zipcode"/>

      <div>
        <button
          type="button"
          className="btn"
          onClick={previousPage}>
            Previous
        </button>
        {' '}
        <button
          type="submit"
          className="btn"
          disabled={invalid || submitting}>
          Next
        </button>
      </div>
    </form>
  )
}

export default reduxForm({
  form: "register",
  destroyOnUnmount: false,
  validate: RegisterValidate
})(RegisterShipAddress)
