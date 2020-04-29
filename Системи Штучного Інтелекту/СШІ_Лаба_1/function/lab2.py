lowTip = 0.05
averTip = 0.15
highTip = 0.25
tipRange = highTip - lowTip

badService = 0
okayService = 3
goodService = 7
greatService = 10
serviceRange = greatService - badService

badFood = 0
greatFood = 10
foodRange = greatFood - badFood

price = float(input('Price: '))
service = int(input('Service: '))
food = int(input('Food: '))

const = (1 - serviceRange) * (tipRange / foodRange * food + lowTip)
if service < okayService:
    tip = (((averTip - lowTip) / (okayService - badService)) * service + lowTip) * serviceRange + const
elif service < goodService:
    tip = averTip * serviceRange + const
else:
    tip = (((highTip - averTip) / (greatService - goodService)) * (
            service - goodService) + averTip) * serviceRange + const

print(f'Tips: {round(abs(tip * price), 2)}')
