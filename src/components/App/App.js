import React, { PropTypes } from 'react'
import { NavbarApp } from '../../containers'
import FooterApp from './FooterApp'

const App = ({children}) => (
  <div className="sbox-page-wrapper">
    <NavbarApp />
    <main>{children}</main>
    <FooterApp />
  </div>
)

App.propTypes = {
  children: PropTypes.node.isRequired
}

export default App
