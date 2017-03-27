import React, { Component } from 'react';
import { AppRegistry, Text, TextInput, View, TouchableHighlight, Image } from 'react-native';
import { StyleSheet } from 'react-native';

var Style = StyleSheet.create({
    rootContainer: {
        flex: 1
    },

    displayContainer: {
        flex: 2,
        backgroundColor: '#193441',
        justifyContent: 'center'
    },

    displayText: {
        color: 'white',
        fontSize: 38,
        fontWeight: 'bold',
        textAlign: 'right',
        padding: 20
    },

    inputContainer: {
        flex: 8,
        backgroundColor: '#3E606F'
    },

    inputButton: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        borderWidth: 0.5,
        borderColor: '#91AA9D'
    },

    inputButtonHighlighted: {
        backgroundColor: '#193441'
    },

    inputButtonText: {
        fontSize: 22,
        fontWeight: 'bold',
        color: 'white'
    },

    inputRow: {
        flex: 1,
        flexDirection: 'row'
    }
});
class InputButton extends Component {
    
    render() {
        return (
            <TouchableHighlight style={[Style.inputButton, this.props.highlight ? Style.inputButtonHighlighted : null]}
                                underlayColor="#193441" onPress={this.props.onPress}>
                <Text style={Style.inputButtonText}><Image source={{uri: this.props.url}} style={{width: 100, height: 100}}/> </Text>
            </TouchableHighlight>
        )
    }
    
}

class Bananas extends Component {
  constructor(props) {
    super(props);
    this.state = {result:'beginning', selectedSymbol:'', computer:'', computerUrl:'https://facebook.github.io/react/img/logo_og.png'};
    this.option = [{'key':'scissors', 'url': 'http://elearning.slps.ntpc.edu.tw/6/100/samples/%E7%AC%AC04%E7%AB%A0-%E5%89%AA%E5%88%80%E7%9F%B3%E9%A0%AD%E5%B8%83%E7%8C%9C%E6%8B%B3/%E9%80%A0%E5%9E%8B/%E5%89%AA%E5%88%80-%E9%BB%83.png'},{'key':'stone', 'url': 'http://elearning.slps.ntpc.edu.tw/6/100/samples/%E7%AC%AC04%E7%AB%A0-%E5%89%AA%E5%88%80%E7%9F%B3%E9%A0%AD%E5%B8%83%E7%8C%9C%E6%8B%B3/%E9%80%A0%E5%9E%8B/%E7%9F%B3%E9%A0%AD-%E9%BB%83.png'},{'key':'paper', 'url': 'http://elearning.slps.ntpc.edu.tw/6/100/samples/%E7%AC%AC04%E7%AB%A0-%E5%89%AA%E5%88%80%E7%9F%B3%E9%A0%AD%E5%B8%83%E7%8C%9C%E6%8B%B3/%E9%80%A0%E5%9E%8B/%E5%B8%83-%E9%BB%83.png'}];
  }

  render() {
    return (
      <View style={{padding: 10}}>
        <View style={Style.inputContainer}>
            <InputButton url={this.state.computerUrl}/>;
        </View>
        <Text style={{padding: 10, fontSize: 42}}>
          {this.state.result}
        </Text>
        <View style={Style.inputContainer}>
            {this._renderInputButtons()}
        </View>
      </View>
    );
  }

  randomInt(max) {
    return Math.floor(Math.random() * (max));
  }

  _renderInputButtons() {
    let inputRow = this.option.map((dict, index) => {
        return <InputButton
                          url={dict['url']}
                          highlight={this.state.selectedSymbol == dict['key']}
                          onPress={this._onInputButtonPressed.bind(this, dict['key'])}
                          key={'butt-' + index} />;
    });    
    return <View style={Style.inputRow}>{inputRow}</View>;
  }

  _onInputButtonPressed(key) {

      let randomRum = this.randomInt(2)
      this.setState({
          selectedSymbol: key,
          computer: this.option[randomRum]['key'],
          computerUrl:this.option[randomRum]['url']
      }, ()=> {
        if(this.state.selectedSymbol == this.state.computer){
          this.setState({
            result:'Tie'
          })
        }
        else if((this.state.selectedSymbol == 'scissors' && this.state.computer=='paper')  || (this.state.selectedSymbol == 'paper' && this.state.computer == 'stone') || (this.state.selectedSymbol == 'stone' && this.state.computer == 'scissors')){
          this.setState({
            result:'Win'
          })
        }
        else{
          this.setState({
            result:'Lose'
          })
        }
      });
  }
}

AppRegistry.registerComponent('Bananas', () => Bananas);