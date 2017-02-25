import mraa
import urllib2
x = mraa.Gpio(44)
x.dir(mraa.DIR_OUT)

true = 1
while(true):
                try:
                        response = urllib2.urlopen('http://linkit7688-smarthome.azurewebsites.net/')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                print status
                if status=='ON':
                                x.write(1)
                elif status=='OFF':
                                x.write(0))
