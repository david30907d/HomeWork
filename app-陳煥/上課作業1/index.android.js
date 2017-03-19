import React, { Component } from 'react';
import { AppRegistry, Text, TextInput, View, TouchableHighlight } from 'react-native';
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
            <TouchableHighlight style={[Style.inputButton, Style.inputButtonHighlighted]}
                                underlayColor="#193441" onPress={this.props.onPress}>
                <Text style={Style.inputButtonText}>{this.props.value}</Text>
            </TouchableHighlight>
        )
    }
    
}

class PizzaTranslator extends Component {
  constructor(props) {
    super(props);
    this.state = {input: "", tmpInput:""};
  }

  render() {
    return (
      <View style={{padding: 10}}>
        <TextInput
          style={{height: 40}}
          placeholder="輸入框"
          onChangeText={(tmpInput) => this.setState({tmpInput})}
        />
        <Text style={{padding: 10, fontSize: 42}}>
          結果:{this.state.input ? this.state.input : ""}
        </Text>
        <InputButton
            value="run"
            onPress={this._onInputButtonPressed.bind(this, "run")}
        />
        <InputButton
            value="clear"
            onPress={this._onInputButtonPressed.bind(this, "clear")}
        />
      </View>
    );
  }

  _onInputButtonPressed(input) {
      if (this.state.input == "" && this.state.tmpInput == ""){
          confirm('確定要退出?')
      }
      switch (input) {
          case 'run':
              let i = this.state.tmpInput
              return this.setState({input:i, tmpInput:""})
          default:
              return this.setState({input:"", tmpInput:""})
      }
  }
}

AppRegistry.registerComponent('PizzaTranslator', () => PizzaTranslator);
