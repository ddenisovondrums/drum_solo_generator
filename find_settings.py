import user_settings
from backend import generate_piece

# finding settings for needed result
target = [False, False, True, False, False, True, False, True,
False, True, False, True, True, False, True, False,
False, True, False, True, False, False, True, False,
False, False, True, False, False, True, True, True,]

piece = generate_piece()

# target = [True, False, False, False]

settings_not_found = True

for i in range(10000000):
    print(user_settings.user_seed)
    result = []
    for bar in piece:
        for beat in bar:
            for note in beat:
                result.append(note['its_pause'])
    # print(result)
    # if len(result) != len(target):
    #     print('WRONG LEN')
    #     break

    if result == target:
        print('..........................WOW..........................')
        settings_not_found = False
        break
    else:
        user_settings.user_seed = "Ted Reed's syncopation - " + str(i)
        piece = generate_piece()


# user_settings.user_seed = 'mr.Ted Reed #' + str(i)
# user_settings.user_seed = 'Ted Reed - ' + str(i) x 10000000
# user_settings.user_seed = "Ted Reed's syncopation #" + str(i) x 5000000000 CRASH WINDOWS
# user_settings.user_seed = "Ted Reed's syncopation - " + str(i) x 11327198

# 2^32 = 4'294'967' 296