import pawLogo from '/paw-icon.png';
import './Header.css'

 export default function Header() {
  return (
    <>
      <a><img src={pawLogo} className="logo"/><h1>Pet Matcher</h1></a>
      <div>header</div>
    </>
  )
}
