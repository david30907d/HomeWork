/*
This is a view i use in a test app,
very useful to list all the use cases
*/

import React, { Component } from 'react';

import {
  AppRegistry,
  StyleSheet,
  Text,
  View,ScrollView,Image, Alert, Button
} from 'react-native';


import { Form,
  Separator,InputField, LinkField,
  SwitchField, PickerField,DatePickerField,TimePickerField
} from 'react-native-form-generator';

export class AwesomeProject extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      formData:{}
    }
  }
  handleFormChange(formData){
    /*
    formData will contain all the values of the form,
    in this example.

    formData = {
    last_name:"",
    gender: '',
    birthday: Date,
    has_accepted_conditions: bool
    }
    */

    this.setState({formData:formData})
    this.props.onFormChange && this.props.onFormChange(formData);
  }
  handleFormFocus(e, component){
    //console.log(e, component);
  }
  openTermsAndConditionsURL(){

  }
  render(){
    let pic = {
      uri: 'https://upload.wikimedia.org/wikipedia/zh/thumb/0/06/THSR.svg/1280px-THSR.svg.png'
    };
    return (<ScrollView keyboardShouldPersistTaps="always" style={{paddingLeft:10,paddingRight:10, height:200}}>
      <Image source={pic} style={{width: 193, height: 110}}/>
      <Form
        ref='registrationForm'
        onFocus={this.handleFormFocus.bind(this)}
        onChange={this.handleFormChange.bind(this)}
        label="Personal Information">
        <Separator label="姓名"/>        
        <InputField ref='last_name' placeholder="請輸入您的姓名: "/>
        <PickerField ref='gender'
          label='性別'
          options={{
            "": '',
            male: '男生',
            female: '女生'
          }}/>
        <PickerField ref='startstation'
          label='起站'
          options={{
            "": '',
            taichung: '台中',
            tainan: '台南'
          }}/>
        <PickerField ref='endstations'
          label='迄站'
          options={{
            "": '',
            taichung: '台中',
            tainan: '台南'
          }}/>
        <PickerField ref='ticket'
          label='票種  全票  兒童票'
          options={{
            "": '',
            children: '兒童票',
            adult: '成人票'
          }}/>
        <Separator />
        <SwitchField label='想收到email 確認'
          ref="has_accepted_conditions"
          helpText='請在下方輸入您的信箱'/>
        <InputField ref='email' placeholder="Email:"/>
      </Form>
      <Button
        onPress={() => {
  Alert.alert('訂購成功')}}
        title="訂購"
        color="#841584"
        accessibilityLabel="Learn more about this purple button"
      />
      </ScrollView>);
    }
  }

  AppRegistry.registerComponent('AwesomeProject', () => AwesomeProject);
