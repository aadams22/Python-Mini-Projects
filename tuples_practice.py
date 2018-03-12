def Sort(T):
  if not T:
	  return ()
  elif len(T) == 1:
	  return (T[0],)
  else:
	  m = Maximum(T)
	  r = Remove(T,m)
	  if len(r) == 1:
		  return r + (m,)
	  else:
		  return Sort(r) + (m,)


def Maximum(T):
  if not T:
	  return ()
  elif len(T) == 1:
	  return T[0]
  elif T[0] <= T[1]:
	  return Maximum(T[1:])
  else:
	  return (Maximum((T[0],) + T[2:]))


def Remove(T,E):
  if not T:
	  return ()
  elif E not in T:
	  return T
  elif T[0] == E:
	  return T[1:]
  else:
	  return ((T[0],) + Remove(T[1:],E))
  

