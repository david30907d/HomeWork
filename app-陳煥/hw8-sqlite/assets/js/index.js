var React = require('react')
var ReactDOM = require('react-dom')
import { Button, Flag, Segment, Header, Icon, Image } from 'semantic-ui-react'

const FlagExampleFlag = () => (
  <Segment>
    <Flag name='myanmar' />
  </Segment>
)

const HeaderExampleUsersIcon = () => (
  <div>
    <Header as='h2' icon textAlign='center'>
      <Icon name='users' circular />
      <Header.Content>
        進入sqlite操作介面
      </Header.Content>
    </Header>
    <Image centered size='large' src='http://cdn02.androidauthority.net/wp-content/uploads/2015/04/sqlite-and-Android-792x446.jpg' />
  </div>
)

class Hello extends React.Component {
    render() {
        return (
            <div>
	            <h1>歡迎使用sqlite demo作業<FlagExampleFlag/></h1>
	            <HeaderExampleUsersIcon/>
            </div>
        )
    }
}

ReactDOM.render(<Hello />, document.getElementById('container'))