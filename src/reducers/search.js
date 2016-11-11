import {
  SEARCH_PRODUCT_REQUEST,
  SEARCH_PRODUCT_SUCCESS,
  SEARCH_PRODUCT_FAILURE,

  CLEAR_SEARCH
} from 'actionTypes'

const initialState = {
  result: [],
  isLoading: false,
  error: false
}

const search = (state = initialState, action) => {
  switch(action.type) {
    case SEARCH_PRODUCT_REQUEST:
      return ({
        ...state,
        isLoading: true
      })

    case SEARCH_PRODUCT_SUCCESS:
      return ({
        result: action.payload,
        isLoading: false,
        error: false
      })
    case SEARCH_PRODUCT_FAILURE:
      return ({
        result: [],
        isLoading: false,
        error: true
      })

    case CLEAR_SEARCH:
      return initialState

    default:
      return state
  }
}

export default search
